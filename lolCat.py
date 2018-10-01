import os



def main():
	# print the header
	# get or create output
	# download cats
	# display cats
	#print('hello from main')
	get_or_create_output_folder()


def print_header():
	print('---------------------------')
	print('          CAT FACTORY')
	print('---------------------------')


def get_or_create_output_folder():
	#print(__file__)
	base_folder = os.path.dirname(__file__)
	print(base_folder)
	folder = 'cat_pictures'
	full_path = os.path.abspath(os.path.join('.', folder))
	#print(os.path.exists(full_path))
	#print(full_path)


if __name__ == '__main__':
	main()