from config_default import file_dir

if __name__ == '__main__':

    associate_file = file_dir['data_dir_tube']

    fh = open(associate_file, 'w')
    N = 50
    for i in range(35, N+35):
        data_dir = "./data/capture_images_" + str(i) + ".jpg\n"
        fh.write(data_dir)

    fh.close()

