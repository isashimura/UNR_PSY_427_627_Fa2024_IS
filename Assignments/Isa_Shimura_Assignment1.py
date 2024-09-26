# %% importing libraries
import random
import os
import matplotlib.pyplot as plt

# %% path to folder with images
fdir = r'C:\Users\isash\OneDrive - University of Nevada, Reno\Fall 2024\PSY 427 Comp App\fLoc_stimuli\fLoc_stimuli'

# %% load images into var

all_img = os.listdir(fdir)

# %% select random 12 images

rnd_img = random.sample(all_img, 12)

# %% load images into list

imgs = []
for img_file in rnd_img:
    path_img = os.path.join(fdir, img_file)
    img = plt.imread(path_img)
    imgs.append(img)
    
# %% subplots and insert images into that

fig, axs = plt.subplots(3, 4, figsize = (15, 10))
for i in range(len(imgs)):
    ax = axs.flatten()[i]
    num_img = imgs[i]
    ax.imshow(num_img, cmap = 'gray')
    ax.axis('off')
    
# %% minimize white space & show result

plt.tight_layout()
plt.show()
