# Welcome!

## Dependence
``` Shell
pip install selenium
sudo apt install Xvfb
pip install xvfbwrapper
```
Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and put it in the same folder or just use the one I support. You can also change the path in transPDF.py

## word-replacer.txt
Feel free to add your word map in word-replacer.txt

## Run it !
First you should create a txt from PDF. Name it as 'raw.txt', such as:
```
Weakly supervised learning with only coarse labels can
obtain visual explanations of deep neural network such as
attention maps by back-propagating gradients. These at-
tention maps are then available as priors for tasks such as
object localization and semantic segmentation. In one com-
mon framework we address three shortcomings of previous
approaches in modeling such attention maps: We (1) first
time make attention maps an explicit and natural compo-
nent of the end-to-end training, (2) provide self-guidance di-
rectly on these maps by exploring supervision form the net-
work itself to improve them, and (3) seamlessly bridge the
gap between using weak and extra supervision if available.
Despite its simplicity, experiments on the semantic segmen-
tation task demonstrate the effectiveness of our methods.
We clearly surpass the state-of-the-art on Pascal VOC 2012
val. and test set. Besides, the proposed framework pro-
vides a way not only explaining the focus of the learner
but also feeding back with direct guidance towards specific
tasks. Under mild assumptions our method can also be un-
derstood as a plug-in to existing weakly supervised learners
to improve their generalization performance.
```
and run
```
python transPDF.py
```
