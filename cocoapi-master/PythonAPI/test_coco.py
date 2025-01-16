from pycocotools.coco import COCO
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Step 1: Load COCO annotations and images
annotation_file = "C:/Users/Nguye/OneDrive/Documents/IRL/COMM2495 Pro Writing/AS3/annotations1/instances_val2017.json/instances_val2017.json"
coco = COCO(annotation_file)

# Step 2: Get all image IDs in the dataset
img_ids = coco.getImgIds()

# Step 3: Get category names
cat_ids = coco.getCatIds()
categories = coco.loadCats(cat_ids)

# Create a dictionary of category ID -> category name
category_names = {category['id']: category['name'] for category in categories}

# Step 4: Loop through each image and visualize annotations
for img_id in img_ids:
    img_info = coco.loadImgs(img_id)[0]

    # Get annotations for the image
    ann_ids = coco.getAnnIds(imgIds=img_info['id'], iscrowd=None)
    annotations = coco.loadAnns(ann_ids)

    # Visualize the image and its bounding boxes with labels
    image_path = f'C:/Users/Nguye/OneDrive/Documents/IRL/COMM2495 Pro Writing/AS3/annotations1/val2017/val2017/{img_info["file_name"]}'
    img = Image.open(image_path)

    # Create the figure and axes
    fig, ax = plt.subplots(1)

    # Display the image
    ax.imshow(img)

    # Loop through annotations and plot bounding boxes with labels
    for ann in annotations:
        bbox = ann['bbox']
        x, y, width, height = bbox
        rect = patches.Rectangle((x, y), width, height, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        # Add category label above each bounding box
        category_name = category_names[ann['category_id']]
        ax.text(x, y - 10, category_name, color='red', fontsize=10, fontweight='bold', backgroundcolor='white')

    # Show the image
    plt.show()
