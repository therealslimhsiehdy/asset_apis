[![LinkedIn][linkedin-shield]][linkedin-url]
</br>

# Asset APIs

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

We have a store of Asset objects -- Asset types can either be Satellites or Antennas, and they have specified Asset classes that match a corresponding Asset type.

Here are the 3 endpoints for the server with examples of requests you can make:

**POST /assets** -- creating an Asset
NOTE: This endpoint requires form data as the body, ie {"asset_name": "name_here", "asset_type": "satellite", "asset_class": "dove"}

**GET /assets** -- showcases all the Assets we have

**GET /assets/{name}** -- showcases the Asset information for a specified Asset name that's the user provides




### Built With

* [Python](https://www.python.org/downloads/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Pytest](https://docs.pytest.org/en/stable/)

<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Create a Python virtual environment:
  ```sh
  python -m venv .venv
  source .venv/bin/activate
   ```

2. Install requirements into virtual environment:
  ```sh
  pip install -r requirements.txt
  ```

3. Start the Flask application:
  ```sh
  FLASK_APP=main.py flask run
  ```

4. Use this link to make requests to the server (Postman suggested):
  ```sh
  http://127.0.0.1:5000
  ```

### Testing
* Run Pytest with the virtual environment activated:
  ```sh
  pytest
  ```

### Thoughts
If this assignment were in "real life" enterprise work, instead of in memory storing with the dictionary data structure, I would choose to store the information in a database. 
For example, if you ended an in memory server you'd lose all your information. However, if you have a database with corresponding Flask API servers, you wouldn't lose all your information.

<!-- CONTACT -->
## Contact

Rebecca Hsieh - rebecca.hsieh07@gmail.com - therealslimhsiehdy.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/therealslimhsiehdy