# ASUP Analysis

A Streamlit-based web application for analyzing NetApp AutoSupport (ASUP) files, providing insights into system hierarchy and network port performance.

## Description

ASUP Analysis is a comprehensive tool designed to parse and visualize NetApp AutoSupport files. The application offers two main analysis capabilities:

1. **System Hierarchy Visualization** - Interactive tree visualization of system configuration and component hierarchy
2. **Port Flapping Analysis** - Detection and visualization of network port state changes and performance issues

## Intent

This tool was created to help NetApp administrators and engineers quickly analyze ASUP files without manual parsing. It transforms complex log data into intuitive visualizations that make it easier to identify system issues, understand configuration hierarchies, and track port performance over time.

## Features

- **File Upload Interface** - Simple drag-and-drop file upload for ASUP files
- **Interactive Visualizations** - Dynamic charts using Plotly for enhanced data exploration
- **System Hierarchy Tree** - Icicle chart visualization showing system component relationships
- **Port Performance Tracking** - Time-series analysis of port state changes and flapping events
- **Multi-page Navigation** - Organized interface with dedicated pages for different analysis types
- **NetApp Branding** - Professional interface with NetApp logo and styling

## Use Cases

### System Configuration Analysis
- Visualize complex system hierarchies and component relationships
- Understand storage system architecture and configuration
- Identify configuration anomalies or inconsistencies

### Network Troubleshooting
- Detect port flapping events and frequency patterns
- Analyze network stability over time
- Identify problematic ports or nodes requiring attention

### Performance Monitoring
- Track port state changes and their frequency
- Monitor system stability trends
- Generate reports for capacity planning and maintenance

## Requirements

### System Requirements
- Python 3.10 or higher
- Web browser (Chrome, Firefox, Safari, Edge)
- Minimum 4GB RAM recommended
- Network connectivity for initial setup

### Python Dependencies
```
streamlit>=1.45.1
pandas>=2.2.3
plotly>=6.1.0
matplotlib>=3.10.3
graphviz>=0.20.3
icecream>=2.1.4
```

## Installation

### Using UV (Recommended)
```bash
# Clone the repository
git clone <repository-url>
cd ASUP_Analysis

# Install dependencies with UV
uv sync
```

### Using Pip
```bash
# Clone the repository
git clone <repository-url>
cd ASUP_Analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r src/requirements.txt
```

## Usage

### Starting the Application
```bash
# Using UV
uv run streamlit run src/asup_views.py

# Or using Python directly
python -m streamlit run src/asup_views.py
```

### Using the Application

1. **Launch the App** - Open your web browser to `http://localhost:8501`

2. **Upload ASUP File** - Use the sidebar file uploader to select your ASUP file

3. **Navigate Pages**:
   - **System Hierarchy** - View interactive tree visualization of system components
   - **Port Flapping** - Analyze network port performance and stability

4. **Interact with Visualizations**:
   - Hover over chart elements for detailed information
   - Use zoom and pan controls for detailed exploration
   - Filter data using interactive controls

## File Structure

```
ASUP_Analysis/
   README.md
   main.py                     # Entry point
   pyproject.toml             # Project configuration
   src/
      asup_views.py          # Main Streamlit application
      home.py                # Home page components
      components/            # Reusable UI components
         netapp_page.py     # NetApp branding components
         netapp_logo.png    # NetApp logo asset
      pages/                 # Streamlit pages
         01_#_System Hierachy.py  # System hierarchy analysis
         02_#_Port_Flapping.py    # Port flapping analysis
      graphs/                # Visualization utilities
         graph_dataframe.py # DataFrame plotting utilities
         graph_as_tree.py   # Tree visualization utilities
      utils/                 # Utility functions
          preprocess.py      # Data preprocessing utilities
   uv.lock                    # UV lock file
```

## Data Format

The application expects NetApp ASUP files in text format containing:
- EMS log entries with timestamp information
- System hierarchy data with indented structure
- Port status and event information

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is provided as-is for NetApp ASUP analysis purposes.

## Support

For issues, questions, or feature requests, please create an issue in the project repository.
