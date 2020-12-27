from PIL import ImageFont

references_table = [{'img': 'assets/1C.png',
                     'confidence': 0.95},

                    {'img': 'assets/55.png',
                     'confidence': 0.95},

                    {'img': 'assets/BD.png',
                     'confidence': 0.95},

                    {'img': 'assets/E9.png',
                     'confidence': 0.94},

                    {'img': 'assets/7A.png',
                     'confidence': 0.95},

                    {'img': 'assets/FF.png',
                     'confidence': 0.95},
                    ]

references_reqs = [{'img': 'assets/1Cs.png',
                    'confidence': 0.9},

                   {'img': 'assets/55s.png',
                    'confidence': 0.9},

                   {'img': 'assets/BDs.png',
                    'confidence': 0.9},

                   {'img': 'assets/E9s.png',
                    'confidence': 0.9},

                   {'img': 'assets/7As.png',
                    'confidence': 0.9},

                   {'img': 'assets/FFs.png',
                    'confidence': 0.9},
                   ]

elements_size = [16, 25, 36, 49]

font = ImageFont.truetype("arial.ttf", 30)

click_delay = 0.1
