"""Testing with streamlit.
```bash
streamlit run test_streamlit.py
``` """
import sys
sys.path.append('pygwalker')
import os
import pandas as pd
import pygwalker as pyg


HERE = os.path.dirname(__file__)

df = pd.read_csv(os.path.join(HERE, "bike_sharing_dc.csv"), parse_dates=['date'])
# df
# pyg.walk(df, env='Streamlit')

html = pyg.to_html(df)
html += """
<script>
window.addEventListener("load", function() {
    window.alert("Hello Selenium!");
  });
</script>
"""
pyg.gwalker.display_html(html, env='Streamlit')