"""
Code to Create Word Cloud Based on frequency column for LinkedIn Profile

Author: Ashish
Created on: 19-Jan-2021
Version: 1.0

GitHub: https://www.linkedin.com/in/ashish568/
LinkedIn: https://github.com/ashishkr568
Medium: https://medium.com/@ashish.568

"""

# Import Packages
import random
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Variables
skills_csv_path = "skills.csv"
output_filename = "LinkedIn_BG_Img"


# Function to re-color generated image
# Change the value in randint to have variation in grey
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(80, 100)


# Function to create  Wordcloud
def create_wordcloud(fpath, f_name):
    # Read Skills dataset
    df = pd.read_csv(fpath)

    # Wordcloud from frequency accepts dictionary
    inp_dict = dict([tuple(x) for x in df.values])

    # Create Word Cloud (The Frame size is as per LinkedIn Background Photo Requirement
    # colormap ['rainbow','Set2']
    wordcloud = WordCloud(width=1596,
                          height=400,
                          colormap='Set2',
                          background_color='#0077b5',
                          min_font_size=20,
                          max_font_size=150,
                          random_state=5).generate_from_frequencies(inp_dict)

    # Plot and Save Figure
    plt.figure(figsize=(40, 5))
    plt.imshow(wordcloud)
    plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
    plt.axis("off")
    plt.savefig(f_name + ".png", bbox_inches='tight', dpi=500)
    plt.show()
    plt.close()


if __name__ == '__main__':
    create_wordcloud(fpath=skills_csv_path, f_name=output_filename)
