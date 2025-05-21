import plotly.express as px
import pandas as pd
import re
import streamlit as st
import io


def parse_hierarchical_file(contents):
    """
    Parses a hierarchical key-value file where hierarchy is indicated by indentation (tabs or spaces).
    Returns a list of dictionaries with 'id', 'parent', and 'label' for tree visualization.
    """
    tree_nodes = []
    parent_stack = []  # Stack to keep track of parent nodes at each level
    node_id_counter = 0  # Unique ID for each node

    with io.StringIO(contents) as file_handle:
        for line in file_handle:
            # Skip empty lines
            if not line.strip():
                continue
            
            line = convert_leading_spaces_to_tabs(line)


            # Count leading spaces or tabs to determine the level
            stripped_line = line.lstrip('\t ')
            indentation = len(line) - len(stripped_line)
            # For mixed tabs/spaces, you may want to normalize (e.g., 4 spaces = 1 tab)
            level = indentation // 1  # Adjust if your file uses a different indent width

            # Use the line itself as the label, or split into key/value for clarity
            if ':' in stripped_line:
                key, value = stripped_line.split(':', 1)
                label = f"{key.strip()}: {value.strip()}"
            else:
                label = stripped_line.strip()

            # Generate a unique node ID
            node_id = f"node_{node_id_counter}"
            node_id_counter += 1

            # Determine parent node
            if level == 0:
                parent_id = ""
                parent_stack = [node_id]  # Reset stack for new top-level node
            else:
                # Ensure the stack is the right size for the current level
                if len(parent_stack) > level:
                    parent_stack = parent_stack[:level]
                parent_id = parent_stack[-1] if parent_stack else ""
                parent_stack.append(node_id)

            # Add node to the list
            tree_nodes.append({
                "id": node_id,
                "parent": parent_id,
                "label": label
            })

    return tree_nodes

def convert_leading_spaces_to_tabs(line, spaces_per_tab=4):
    """
    Converts leading spaces in a line to tabs, one tab per 'spaces_per_tab' spaces.
    Only affects leading spaces, not spaces within the line.
    """
    # Match leading spaces
    match = re.match(r'^( *)', line)
    if match:
        leading_spaces = match.group(0)
        num_tabs = len(leading_spaces) // spaces_per_tab
        remainder_spaces = len(leading_spaces) % spaces_per_tab
        new_leading = '\t' * num_tabs + ' ' * remainder_spaces
        return new_leading + line[len(leading_spaces):]
    else:
        return line




def visualize_tree(tree_nodes):
    """
    Visualizes the hierarchy as a tree using Plotly icicle chart.
    """
    data_frame = pd.DataFrame(tree_nodes)
    fig = px.icicle(
        data_frame,
        names='label',
        parents='parent',
        ids='id',
        # Optionally, you can add custom_data for hover
    )
    # Set the figure size here
    fig.update_layout(
        title="System Configuration Hierarchy",
        margin=dict(t=50, l=25, r=25, b=25),
        width=1200,   # Set desired width in pixels
        height=1700    # Set desired height in pixels
    )
    st.plotly_chart(fig, use_container_width=True)    
    
def analyse_tree():
    """
    """
    nodes = parse_hierarchical_file(st.session_state['uploaded_data'])
    visualize_tree(nodes)


uploaded_files = st.sidebar.file_uploader("Drop a ASUP file here", 
                                          type=None, 
                                          accept_multiple_files=False)

if uploaded_files is not None:
    # Read the contents of the uploaded file
    file_contents = uploaded_files.read()
    # Decode the bytes to a string
    file_contents = file_contents.decode('utf-8')
    # Store the contents in session state
    print(file_contents)
    st.session_state['uploaded_data'] = file_contents
    
    analyse_tree()