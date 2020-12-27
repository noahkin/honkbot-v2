import io
import json
import discord
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
import requests

class GooseID:
    def __init__(self):
        self.imagenet_class_index = json.load(open('neural/static/imagenet_class_index.json'))
        self.model = models.densenet121(pretrained=True)
        self.model.eval()


    def transform_image(self, image_bytes):
        my_transforms = transforms.Compose([transforms.Resize(255),
                                            transforms.CenterCrop(224),
                                            transforms.ToTensor(),
                                            transforms.Normalize(
                                                [0.485, 0.456, 0.406],
                                                [0.229, 0.224, 0.225])])
        image = Image.open(io.BytesIO(image_bytes))
        return my_transforms(image).unsqueeze(0)


    def get_prediction(self, image_bytes):
        tensor = self.transform_image(image_bytes=image_bytes)
        outputs = self.model.forward(tensor)
        _, y_hat = outputs.max(1)
        predicted_idx = str(y_hat.item())
        return self.imagenet_class_index[predicted_idx]


    def get_class(self, img_bytes):
        class_id, class_name = self.get_prediction(image_bytes=img_bytes)
        return class_name

    def check_url(self, url):
        try:
            r = requests.get(url, stream = True)
            if r.status_code == 200:
                print('request error')
                return self.get_class(r.content)
            return False
        except Exception as e:
            print(e)
            return False
            
    async def goose_reaction(self, message, msgContent):
        await message.channel.send('o shit is that a pic of a goose?')

    async def other_reaction(self, message, msgContent, class_name):
        await message.channel.send("yo that's a " + class_name)