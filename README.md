# Welcome!

## Dependence
``` Shell
pip install selenium
sudo apt install xvfb
pip install xvfbwrapper
```
Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and put it in the same folder or just use the one I support. You can also change the path in transPDF.py

And also, you should make sure you can touch https://translate.google.com/?tr=f&#en/zh-CN/

## word-replacer.txt
Feel free to add your word map in word-replacer.txt

## Run it !
First you should create a txt from PDF. Name it as 'raw.txt', such as:
```
1. Introduction

Weakly supervised learning [3, 26, 33, 35] has recently
gained much attention as a popular solution to address la-
beled data scarcity in computer vision. Using only image
level labels for example, one can obtain attention maps for a
given input with back-propagation on a Convolutional Neu-
ral Network (CNN). These maps relate to the network’s re-
sponse given specific patterns and tasks it was trained for.
The value of each pixel on an attention map reveals to what
extent the same pixel on the input image contributes to the
final output of the network. It has been shown that one
can extract localization and segmentation information from
such attention maps without extra labeling effort.

However, supervised by only classification loss, atten-
tion maps often only cover small and most discriminative
regions of object of interest [11, 28, 38]. While these at-
tention maps can still serve as reliable priors for tasks like
segmentation [12], having attention maps covering the tar-
get foreground objects as complete as possible can further
boost the performance. To this end, several recent works ei-
ther rely on combining multiple attention maps from a net-
work via iterative erasing steps [31] or consolidating atten-
tion maps from multiple networks [11]. Instead of passively
exploiting trained network attention, we envision an end-to-
end framework with which task-specific supervision can be
directly applied on attention maps during training stage.
```
and run
```
python3 transPDF.py
```
