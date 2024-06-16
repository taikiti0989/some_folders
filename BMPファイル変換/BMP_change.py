# from PIL import Image

# def convert_to_8bit_palette(input_path, output_path):
#     # 画像を読み込む
#     img = Image.open(input_path)
    
#     # 8bitパレットモードに変換
#     img_8bit = img.convert("P", palette=Image.ADAPTIVE, colors=256)
    
#     # 変換された画像を保存
#     img_8bit.save(output_path, format='BMP')

# # 入力BMPファイルのパス
# input_path = 'input_bmp_image.bmp'
# # 出力BMPファイルのパス
# output_path = 'output_image_8bit_palette.bmp'

# # 画像を変換して保存
# convert_to_8bit_palette(input_path, output_path)


import os
import glob
from PIL import Image

def convert_to_8bit_palette(input_folder, output_folder):
    # 入力フォルダ内の全てのBMPファイルを取得
    bmp_files = glob.glob(os.path.join(input_folder, '*.bmp'))

    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 各BMPファイルを変換して出力フォルダに保存
    for bmp_file in bmp_files:
        # 画像を読み込む
        img = Image.open(bmp_file)
        
        # 8bitパレットモードに変換
        img_8bit = img.convert("P", palette=Image.ADAPTIVE, colors=256)
        
        # 出力ファイルのパスを生成
        file_name = os.path.basename(bmp_file)
        output_path = os.path.join(output_folder, file_name)
        
        # 変換された画像を保存
        img_8bit.save(output_path, format='BMP')
        print(f"Converted and saved: {output_path}")

# 入力BMPファイルがあるフォルダのパス
input_folder = 'input_folder'
# 出力BMPファイルを保存するフォルダのパス
output_folder = 'output_folder'

# 画像を変換して保存
convert_to_8bit_palette(input_folder, output_folder)
