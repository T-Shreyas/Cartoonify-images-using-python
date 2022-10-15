class Cartoonizer:

def __init__(self):
pass

def render(self, img_rgb):
img_rgb = cv2.imread(img_rgb)
img_rgb = cv2.resize(img_rgb, (1366,768))
numDownSamples = 2 
numBilateralFilters = 50 

img_color = img_rgb
for _ in range(numDownSamples):
img_color = cv2.pyrDown(img_color)

for _ in range(numBilateralFilters):
img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

for _ in range(numDownSamples):
img_color = cv2.pyrUp(img_color)

