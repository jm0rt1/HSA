# About the Web App

## Running locally

GitHub Copilot: To run the Flask application on your local machine, follow these steps:

1. Save the Python code in a file named `web_app.py` in your project directory.

2. Open a terminal and navigate to your project directory. You can use the `cd` command to change directories. For example:

   ```bash
   cd path/to/your/project/directory
   ```

3. Set the `FLASK_APP` environment variable to `web_app.py`. The command to do this depends on your operating system:

   - On Unix/Linux/macOS:

     ```bash
     export FLASK_APP=web_app.py
     ```

   - On Windows:

     ```cmd
     set FLASK_APP=web_app.py
     ```

4. Run the Flask application with the `flask run` command:

   ```bash
   flask run
   ```

5. Open a web browser and go to `http://localhost:5000`. You should see your Flask application running.

Remember, this assumes that you have already installed Flask and the other necessary packages (`numpy` and `plotly`) in your Python environment. If you haven't, you can install them with pip:

```bash
pip install flask numpy plotly
```

## Troubleshooting JavaScript not shoinwg up:

GitHub Copilot: The issue might be related to the JavaScript file not being loaded or not functioning as expected. Here are a few things you can check:

1. Make sure the `script.js` file is located in the `static/js` directory, and that the directory structure is as follows:

   ```
   /src
       web_app.py
       /templates
           index.html
       /static
           /js
               script.js
   ```

2. Check the JavaScript console in your web browser for any error messages. You can usually open this by right-clicking on the page, selecting "Inspect" or "Inspect Element", and then going to the "Console" tab.

3. Make sure the URL in the AJAX request in `script.js` matches the route in your Flask application. In this case, the URL should be `/update_graph`.

4. Make sure the Flask route `/update_graph` is working correctly. You can test this by sending a POST request to `/update_graph` with the expected JSON data and checking the response.

5. If you're still having trouble, you might want to add some `console.log` statements in your JavaScript code to help debug the issue. For example, you could add `console.log(data);` in the `success` function of the AJAX request to see what data is being returned from the server.