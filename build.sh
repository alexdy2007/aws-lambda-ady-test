~/.local/share/virtualenvs/nr_query_builder-kleVX6AY/lib/python3.9/site-packages
zip -r ~/Projects/nr_query_builder/deployment-package.zip .
cd  ~/Projects/nr_query_builder
zip -g deployment-package.zip lambda_function.py