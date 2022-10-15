class Cartoonizer:

def __init__(self):
pass

def render(self, img_rgb):
img_rgb = cv2.imread(img_rgb)
img_rgb = cv2.resize(img_rgb, (1366,768))
numDownSamples = 2 
numBilateralFilters = 50 
