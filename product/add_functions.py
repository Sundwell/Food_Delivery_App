import os


def get_additional_images_path(instance, filename):
    """

    :param instance: instance of object 'Image'
            :type <image.models.Image>
    :param filename:
    :return:
    """
    return os.path.join(
        f'product/images/{instance.product.name}/additional_photos/{filename}')


def get_image_path(instance, filename):
    """
    :param instance:    instance of object such as object 'apple' which has id
                        type of instance: <product.models.Product>

    :param filename:    just name of the file like 'apple.png'
                        type of filename: <str>

    :return: simply     returning path where django should save our file
    """
    return os.path.join(f'product/images/{instance.name}/main/{filename}')
