#구글 이미지 크롤링 인데 지금 막힘;;; 다른 방법 찾아봐야 할 듯
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)
print(paths)   #printing absolute paths of the downloaded images