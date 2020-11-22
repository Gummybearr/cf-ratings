import requests, json

from .palette import card_color 

def crawl_data(handle):
    crawled_data = requests.get('https://codeforces.com/api/user.info?handles='+handle).json()
    user = {}
    user['handle'] = handle
    user['rank'] = crawled_data['result'][0]['rank']
    return user

def generate_card(user):
    print(user)
    val = '''
        <!DOCTYPE svg PUBLIC 
            "-//W3C//DTD SVG 1.1//EN" 
            "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg width="350" height="175" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <!-- Created with Method Draw - http://github.com/duopixel/Method-Draw/ -->
            <g>
                <title>background</title>
                <rect fill="#fff" id="canvas_background" height="177" width="352" y="-1" x="-1"/>
                <g display="none" overflow="visible" y="0" x="0" height="100%" width="100%" id="canvasGrid">
                    <rect fill="url(#gridpattern)" stroke-width="0" y="0" x="0" height="100%" width="100%"/>
                </g>
            </g>
            <g>
                <title>Layer 1</title>
                <image stroke="null" xlink:href=\"'''+card_color[user['rank']]+'''\" id="svg_1" height="176.99999" width="351.99999" y="-2.5" x="0"/>
            </g>
            <text x="30" y="75" style="font-family:Arial; font-size:20pt; fill:white ">'''+user['handle']+'''</text>
            <text x="30" y="110" style="font-family:Arial; font-size:13pt; fill:white ">'''+user['rank']+'''</text>
        </svg>
        '''
    return val
