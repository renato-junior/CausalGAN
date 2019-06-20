

def get_attributes(f):
    attrs = []
    for line in f:
        attrs.append(line.split(" ")[1].replace("\n", ""))
    return attrs

def get_images_names(f):
    images = []
    for line in f:
        images.append(line.split(" ")[1].replace("\n", "").split("/")[1])
    return images

def create_csv():
    f_in = open("image_attribute_labels.txt", "r")
    f_attr = open("attributes.txt", "r")
    attrs = get_attributes(f_attr)
    f_attr.close()

    f_out = open("out1.csv", "w")

    # Write first line
    f_out.write("image_id,")
    for i in range(len(attrs)-1):
        f_out.write("{},".format(attrs[i]))
    f_out.write("{}\n".format(attrs[len(attrs)-1]))

    # Write actual data to csv
    for image_id in range(1, 11789):
        attr_is_present = []
        for attr_id in range(1, 313):
            line = f_in.readline()
            line_split = line.split(" ")
            attr_is_present.append(line_split[2])
        f_out.write("{},".format(image_id))
        for i in range(len(attr_is_present)-1):
            f_out.write("{},".format(attr_is_present[i]))
        f_out.write("{}\n".format(attr_is_present[len(attr_is_present)-1]))

    f_in.close()
    f_out.close()

def create_txt():
    f_in = open("image_attribute_labels.txt", "r")
    f_attr = open("attributes.txt", "r")
    attrs = get_attributes(f_attr)
    f_attr.close()

    f_images = open("/mnt/62645850645828D5/Ubuntu_files/causalidade_datasets/CUB_200_2011/CUB_200_2011/images.txt", "r")
    img_names = get_images_names(f_images)
    f_images.close()

    f_out = open("list_attr.txt", "w")

    # Write first line
    for i in range(len(attrs)-1):
        f_out.write("{} ".format(attrs[i].replace("::", "-").replace("(", "").replace(")", "")))
    f_out.write("{}\n".format(attrs[len(attrs)-1].replace("::", "-").replace("(", "").replace(")", "")))

    # Write actual data to csv
    for image_id in range(1, 11789):
        attr_is_present = []
        for attr_id in range(1, 313):
            line = f_in.readline()
            line_split = line.split(" ")
            attr_is_present.append(line_split[2])
        f_out.write("{} ".format("{:06d}.jpg".format(image_id)))
        for i in range(len(attr_is_present)-1):
            f_out.write("{} ".format('1' if attr_is_present[i] == '1' else '-1'))
        f_out.write("{}\n".format('1' if attr_is_present[len(attr_is_present)-1] == '1' else '-1'))

    f_in.close()
    f_out.close()

if __name__ == "__main__":
    # create_csv()
    create_txt()