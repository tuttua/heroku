mkdir -p ~/.streamlit/

echo :\
[general]\n\
email = \"21f1001562@student.onlinedegree.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
\n\
" > ~/.streamlit/config.toml
