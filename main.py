import sys
from streamlit.web import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "app/app.py", "--server.headless", "True"]
    sys.exit(stcli.main())