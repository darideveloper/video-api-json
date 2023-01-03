<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Fiverr][fiverr-shield]][fiverr-url]
[![Gmail][gmail-shield]][gmail-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/darideveloper/video_api_json">
    <img src="./imgs/logo.png" alt="Logo" width="250" height="80">
  </a>

<h3 align="center">Video API Json</h3>

  <p align="center">
    Flask app for modify data (CRUD) about films stored in a local json file.
    <br />
    <a href="https://github.com/darideveloper/video_api_json/issues">Report Bug</a>
    ·
    <a href="https://github.com/darideveloper/video_api_json/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#built-with">Api endpoints</a></li>
        <li><a href="#built-with">Api documentation in postman</a></li>
        <li><a href="#built-with">Data structure</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Flask app for modify data (CRUD) about films stored in a local json file.

### Built With


<div>
<a href="https://www.python.org/">
  <img src="https://cdn.svgporn.com/logos/python.svg" width="50" alt="python" title="python">
</a>
<a href="https://flask.palletsprojects.com/en/2.2.x/">
  <img src="https://cdn.svgporn.com/logos/flask.svg" width="50" alt="flask" title="flask">
</a>


### Api endpoints

> (GET) **/all/** - Show all films with pagination. Get params: page (int), results-per-page (int)

> (GET) **/id/** - Show a film. Url param: id (int)

> (POST) **/** - Create a film. Json: custom data structure

> (PUT) **/id/** - Update a film. Json: custom data structure. Url param: id (int)

> (DELETE) **/id/** - Delete a film. Url param: id (int)

### Api doumentation in postman

<a href="https://documenter.getpostman.com/view/14580012/2s8Z711s58">
  <img src="./imgs/postman.png" alt="postman logo" width="160" height="50">
</a>

### Data structure

The project allow all data structure modification and languje, just keep the variable "last_update" in the top, as a string, and "films" like a list of dictionaries.

Sample (english):

```json
{
  "last_update" : "08/06/2022",
  "films": [
      {
          "title": "Pulp fiction",
          "actors": [
  
              {
                  "first_name": "Thurman",
                  "last_name": "Uma"
              },
              {
                  "first_name": "Jackson",
                  "last_name": "Samuel L."
              },
          ]
      },
  ]
}
```

Sample (french):

```json
{
  "last_update" : "08/06/2022",
  "films": [
      {
          "titre": "Pulp fiction",
          "année": 1994,
          "réalisateur": [
            "Tanrantino",
            "Quentin"
          ]
      },
  ]
}
```

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darideveloper/video_api_json.git
   ```
2. Install python packages (opening a terminal in the project folder)
   ```sh
   python -m pip install -r requirements.txt 
   ```

<!-- USAGE EXAMPLES -->
## Usage

1. Open a terminal in the project folder
2. Run the project folder with python: 
    ```sh
    python .
    ```
3. Query the endpoints

<!-- ROADMAP -->
## Roadmap

- [x] CRUD endpoints
  - [x] Create a film
  - [x] Read a film
  - [x] Update a film
  - [x] Delete a film
- [x] Endpoint for show all fimls with pagination

See the [open issues](https://github.com/darideveloper/video_api_json/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Darideveloper - [@developerdari](https://twitter.com/developerdari) - darideveloper@gmail.com.com

Project Link: [https://github.com/darideveloper/video_api_json](https://github.com/darideveloper/video_api_json)


<!-- MARKDOWN LINKS & imgs -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/darideveloper/video_api_json.svg?style=for-the-badge
[contributors-url]: https://github.com/darideveloper/video_api_json/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/darideveloper/video_api_json.svg?style=for-the-badge
[forks-url]: https://github.com/darideveloper/video_api_json/network/members
[stars-shield]: https://img.shields.io/github/stars/darideveloper/video_api_json.svg?style=for-the-badge
[stars-url]: https://github.com/darideveloper/video_api_json/stargazers
[issues-shield]: https://img.shields.io/github/issues/darideveloper/video_api_json.svg?style=for-the-badge
[issues-url]: https://github.com/darideveloper/video_api_json/issues
[license-shield]: https://img.shields.io/github/license/darideveloper/video_api_json.svg?style=for-the-badge
[license-url]: https://github.com/darideveloper/video_api_json/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/
[product-screenshot]: ./imgs/screenshot.gif
[postman-logo]: https://cdn.svgporn.com/logos/postman.svg
[gmail-url]: mailto:darideveloper@gmail.com
[fiverr-url]: https://www.fiverr.com/darideveloper
[gmail-shield]: https://img.shields.io/badge/-gmail-black.svg?style=for-the-badge&logo=gmail&colorB=555&logoColor=white
[fiverr-shield]: https://img.shields.io/badge/-fiverr-black.svg?style=for-the-badge&logo=fiverr&colorB=555&logoColor=white

<span>Last code update: <time datetime="2022-11-29" class="last-update">2023-01-02</time>
