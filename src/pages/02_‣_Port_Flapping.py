import re
import pandas as pd
from datetime import datetime
import pytz
from graphs.graph_dataframe import graph_dataframe
from icecream import ic
import streamlit as st

def parse_asup(content):

    # Split the content into blocks using the separator line
    blocks = content.split('--SmartSolve-- EMS-LOG-FILE.GZ had')
    blocks = [block.strip() for block in blocks if block.strip()]

    # Regular expression to match the log lines of interest
    log_pattern = re.compile(
        r"""
        ^\s*\[\?\]\s+                                   # Line starts with optional spaces and '[?]'
        (?P<date>\w{3}\s+\w{3}\s+\d{2})\s+              # Date, e.g., 'Wed Apr 30'
        (?P<time>\d{2}:\d{2}:\d{2})\s+                  # Time, e.g., '10:44:39'
        (?P<tz>[+-]\d{4})\s+                            # Timezone, e.g., '-0400'
        \[(?P<node>[^\]:]+):                            # Node name inside brackets before first colon
        [^\]]*\]:\s*                                    # Skip to end of bracketed section
        (?P<message>.*?)\s+on\s+node\s+                 # Message up to 'on node'
        (?P=node),\s+port\s+(?P<port>[^\.\s]+)\.        # Node name again, then 'port' and port number
        """,
        re.VERBOSE | re.MULTILINE
    )

    # List to collect all parsed log lines
    parsed_rows = []

    for block_number, block in enumerate(blocks):
        ic(block)
        # Find all matching lines in the block
        for match in log_pattern.finditer(block):
            date_str = match.group('date')
            time_str = match.group('time')
            tz_str = match.group('tz')
            node_name = match.group('node')
            message_text = match.group('message')
            port_number = match.group('port')

            # Combine date, time, and timezone into a datetime object
            datetime_string = f"{date_str} {time_str} {tz_str}"
            try:
                # Try parsing with a fixed year (2025)
                dt = datetime.strptime(datetime_string + " 2025", "%a %b %d %H:%M:%S %z %Y")
            except Exception:
                # Fallback: use current year if parsing fails
                dt = datetime.strptime(datetime_string + f" {datetime.now().year}", "%a %b %d %H:%M:%S %z %Y")
            dt_utc = dt.astimezone(pytz.UTC)

            # Append the parsed data as a dictionary
            parsed_rows.append({
                "Block": block_number,
                "Date": date_str,
                "Time": dt_utc.strftime("%Y-%m-%d %H:%M:%S"),
                "Node": node_name,
                "Port": port_number,
                "Message": message_text
            })

    # Create a DataFrame from all parsed rows
    df = pd.DataFrame(parsed_rows)
    # Group by Date, Node, and Port, and count the number of occurrences
    if not df.empty:
        grouped_df = df.groupby(['Date', 'Node', 'Port'], as_index=False).agg({
            'Block': 'first',  # or you can use list if you want all block numbers
            'Time': 'first',   # or list if you want all times
            'Message': 'first' # or list if you want all messages
        })
        # Add a 'Count' column for the number of occurrences
        grouped_df['Count'] = df.groupby(['Date', 'Node', 'Port']).size().values
    else:
        grouped_df = df  # Empty DataFrame

    return grouped_df

def analyse_portflaps():
    """
    This function analyzes port flaps based on the parsed data.
    It can be extended to include more complex analysis as needed.
    """
    df = parse_asup(st.session_state['uploaded_data'])
    graph_dataframe(df)


analyse_portflaps()