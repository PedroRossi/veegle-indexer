from extractor import Extractor
from indice import index
from indice import compressIndex
from indice import transformJson
import os


def main():
    path = 'pages/positivos'
    recipes = []
    #for domain in os.listdir(path):
        #domain_path = os.path.join(path, domain+'/')
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if full_path.endswith('.html'):
            try:
                e = Extractor(full_path)
                recipe = e.to_dicitonary()
                recipes.append(recipe)
            except:
                print('error in\ndomain: ' + filename + '\nfile: ' + filename + '\n')
    inv_indx_name = index(recipes, 'name')
    transformJson('index_no_compress_name', inv_indx_name)
    inv_indx_ingredients = index(recipes, 'ingredients')
    transformJson('index_no_compress_ingredients', inv_indx_ingredients)
    inv_indx_steps =  index(recipes, 'steps')
    transformJson('index_no_compress_steps', inv_indx_steps)
    inv_indx_name = compressIndex(recipes, 'name')
    transformJson('index_compress_name', inv_indx_name)
    inv_indx_ingredients = compressIndex(recipes, 'ingredients')
    transformJson('index_compress_ingredients', inv_indx_ingredients)
    inv_indx_steps =  compressIndex(recipes, 'steps')
    transformJson('index_compress_steps', inv_indx_steps)


if __name__ == '__main__':
    main()