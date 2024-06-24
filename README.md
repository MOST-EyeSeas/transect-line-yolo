
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">YOLO Transect Line Detector</h3>

  <p align="center">
    A retrained version of YOLO v8 to detect the transect line in diving images. 
    <br />
    <a href="(https://github.com/MOST-EyeSeas/transect-line-yolo/blob/master/val_batch2_pred.jpg)"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>


<!-- GETTING STARTED -->
## Getting Started
![image_mask_bounding_box](https://github.com/MOST-EyeSeas/transect-line-yolo/blob/master/val_batch2_pred.jpg)

- Make sure your system has a GPU with compatible driver+CUDA
- Some other prominent libraries are ultralitics, pytorch and pillow.
- You can also run in using the included Dockerfile, note you must modify the paths in the config.yaml file (lines 4-9) to generate output data.

Input data must be added either split into train/test/val folders, you can also use the included dataset class to split and organise raw data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
Using the Dataset class
Add a folder named "raw_data", within should be a folder "images" including all images and "bounding_box" including bounding boxes data.
Folder structure:
<br>|-- data_raw
<br>|  |-- images
<br>|  |  |-- image1.jpg
<br>|  |  |-- image2.jpg
<br>|  |  |-- ...
<br>|  |-- bounding_box
<br>|  |  |-- image1.txt
<br>|  |  |-- image2.txt
<br>|  |  |-- ...
<br>Next - initiate the Dataset class use save_data method. Voilla!

Training
Run the training lines in the main.py file.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

[@ziv_aharoni](https://www.linkedin.com/in/ziv-aharoni-3909271b0/) - ahaziv@gmail.com

[https://github.com/MOST-EyeSeas/Track-anything-data-producer](https://github.com/MOST-EyeSeas/transect-line-yolo)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: [snake_cube_solution.png](https://github.com/MOST-EyeSeas/Track-anything-data-producer/blob/main/image_mask_bb.JPG)
