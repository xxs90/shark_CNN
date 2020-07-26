def load_images():
	import pandas as pd
	import shutil
	import os

	pd.options.mode.chained_assignment = None

	aquarium_training = pd.read_csv('aquarium_shark_training.csv')
	cyber_training = pd.read_csv('Cyberinitiative_shark_training.csv')
	drawing_test = pd.read_csv('drawing_test.csv')
	drawing_training = pd.read_csv('drawing_training.csv')
	insta_test = pd.read_csv('images_Instagram_shark_test.csv')
	insta_training = pd.read_csv('images_Instagram_shark_training.csv')
	not_shark_test = pd.read_csv('not_shark_test.csv')
	not_shark_training = pd.read_csv('not_shark_training.csv')
	server_test = pd.read_csv('server_images_shark_test.csv')
	server_training = pd.read_csv('server_images_shark_training.csv')
	video_training = pd.read_csv('video_frames_shark_training.csv')

	current = os.getcwd()

	aq_dir = 'aquarium/'
	cyber_dir = 'Cyberinitiative/'
	drawing_dir = 'drawing/'
	insta_dir = 'images_Instagram/'
	not_shark_dir = 'not_shark/'
	server_dir = 'server_images/'
	video_dir = 'video_frames/'

	class_0_test = 'dataset/test_set/drawing/'
	class_1_test = 'dataset/test_set/not_shark/'
	class_2_test = 'dataset/test_set/shark/'

	class_0_training = 'dataset/training_set/drawing/'
	class_1_training = 'dataset/training_set/not_shark/'
	class_2_training = 'dataset/training_set/shark/'

	print('\nLoading images...\n')

	server_label_training = server_training['img'].tolist()
	for i in range(len(server_training)):
		label = server_label_training[i]
		try:
			shutil.move(server_dir + label, class_2_training + label)
		except FileNotFoundError:
			continue
			
	video_label_training = video_training['img'].tolist()
	for i in range(len(video_training)):
		label = video_label_training[i]
		try:
			shutil.move(video_dir + label, class_2_training + label)
		except FileNotFoundError:
			continue

	aq_label = aquarium_training['img'].tolist()
	for i in range(len(aquarium_training)):
		label = aq_label[i]
		try:
			shutil.move(aq_dir + label, class_2_training + label)
		except FileNotFoundError:
			continue

	cyber_label = cyber_training['img'].tolist()
	for i in range(len(cyber_training)):
		label = cyber_label[i]
		try:
			shutil.move(cyber_dir + label, class_2_training + label)
		except FileNotFoundError:
			continue

	insta_label_training = insta_training['img'].tolist()
	for i in range(len(insta_training)):
		label = insta_label_training[i]
		try:
			shutil.move(insta_dir + label, class_2_training + label)
		except FileNotFoundError:
			continue

	os.chdir(class_2_training)
	def listdir_nohidden(path):
	    for f in os.listdir(path):
	        if not f.startswith('.'):
	            yield f
	pwd_list = list(listdir_nohidden(os.getcwd()))

	df = pd.DataFrame(pwd_list, columns=['img'])
	shark_training = str(len(df))
	os.chdir(current)

	print('shark training images loaded')
	print(shark_training + ' trainable shark images\n')

	server_label_test = server_test['img'].tolist()
	for i in range(len(server_test)):
		label = server_label_test[i]
		try:
			shutil.move(server_dir + label, class_2_test + label)
		except FileNotFoundError:
			continue

	insta_label_test = insta_test['img'].tolist()
	for i in range(len(insta_test)):
		label = insta_label_test[i]
		try:
			shutil.move(insta_dir + label, class_2_test + label)
		except FileNotFoundError:
			continue

	os.chdir(class_2_test)
	def listdir_nohidden(path):
	    for f in os.listdir(path):
	        if not f.startswith('.'):
	            yield f
	pwd_list = list(listdir_nohidden(os.getcwd()))

	df1 = pd.DataFrame(pwd_list, columns=['img'])
	shark_test = str(len(df1))
	os.chdir(current)

	print('shark test images loaded')
	print(shark_test + ' testable shark images\n')

	draw_label_training = drawing_training['img'].tolist()
	for i in range(len(drawing_training)):
		label = draw_label_training[i]
		try:
			shutil.move(drawing_dir + label, class_0_training + label)
		except FileNotFoundError:
			continue

	os.chdir(class_0_training)
	def listdir_nohidden(path):
	    for f in os.listdir(path):
	        if not f.startswith('.'):
	            yield f
	pwd_list = list(listdir_nohidden(os.getcwd()))

	df2 = pd.DataFrame(pwd_list, columns=['img'])
	dr_training = str(len(df2))
	os.chdir(current)

	print('drawing training images loaded')
	print(dr_training + ' trainable drawing images\n')

	draw_label_test = drawing_test['img'].tolist()
	for i in range(len(drawing_test)):
		label = draw_label_test[i]
		try:
			shutil.move(drawing_dir + label, class_0_test + label)
		except FileNotFoundError:
			continue

	os.chdir(class_0_test)
	def listdir_nohidden(path):
	    for f in os.listdir(path):
	        if not f.startswith('.'):
	            yield f
	pwd_list = list(listdir_nohidden(os.getcwd()))

	df3 = pd.DataFrame(pwd_list, columns=['img'])
	dr_test = str(len(df3))
	os.chdir(current)

	print('drawing test images loaded')
	print(dr_test + ' testable drawing images\n')

	not_shark_label_training = not_shark_training['img'].tolist()
	for i in range(len(not_shark_training)):
		label = not_shark_label_training[i]
		try:
			shutil.move(not_shark_dir + label, class_1_training + label)
		except FileNotFoundError:
			continue

	os.chdir(class_1_training)
	def listdir_nohidden(path):
	    for f in os.listdir(path):
	        if not f.startswith('.'):
	            yield f
	pwd_list = list(listdir_nohidden(os.getcwd()))

	df4 = pd.DataFrame(pwd_list, columns=['img'])
	non_shark_training = str(len(df4))
	os.chdir(current)

	print('non-shark training images loaded')
	print(non_shark_training + ' trainable non-shark images\n')

	not_shark_label_test = not_shark_test['img'].tolist()
	for i in range(len(not_shark_test)):
		label = not_shark_label_test[i]
		try:
			shutil.move(not_shark_dir + label, class_1_test + label)
		except FileNotFoundError:
			continue

	os.chdir(class_1_test)
	def listdir_nohidden(path):
	    for f in os.listdir(path):
	        if not f.startswith('.'):
	            yield f
	pwd_list = list(listdir_nohidden(os.getcwd()))

	df5 = pd.DataFrame(pwd_list, columns=['img'])
	non_shark_test = str(len(df5))
	os.chdir(current)

	print('non-shark test images loaded')
	print(non_shark_test + ' testable non-shark images\n')


def return_images():
	import pandas as pd
	import shutil
	import os

	pd.options.mode.chained_assignment = None


	print('\nPutting images back... DO NOT CLOSE\n')

	aquarium_training = pd.read_csv('aquarium_shark_training.csv')
	cyber_training = pd.read_csv('Cyberinitiative_shark_training.csv')
	drawing_test = pd.read_csv('drawing_test.csv')
	drawing_training = pd.read_csv('drawing_training.csv')
	insta_test = pd.read_csv('images_Instagram_shark_test.csv')
	insta_training = pd.read_csv('images_Instagram_shark_training.csv')
	not_shark_test = pd.read_csv('not_shark_test.csv')
	not_shark_training = pd.read_csv('not_shark_training.csv')
	server_test = pd.read_csv('server_images_shark_test.csv')
	server_training = pd.read_csv('server_images_shark_training.csv')
	video_training = pd.read_csv('video_frames_shark_training.csv')

	aq_dir = 'aquarium/'
	cyber_dir = 'Cyberinitiative/'
	drawing_dir = 'drawing/'
	insta_dir = 'images_Instagram/'
	not_shark_dir = 'not_shark/'
	server_dir = 'server_images/'
	video_dir = 'video_frames/'

	class_0_test = 'dataset/test_set/drawing/'
	class_1_test = 'dataset/test_set/not_shark/'
	class_2_test = 'dataset/test_set/shark/'

	class_0_training = 'dataset/training_set/drawing/'
	class_1_training = 'dataset/training_set/not_shark/'
	class_2_training = 'dataset/training_set/shark/'

	server_label_training = server_training['img'].tolist()
	video_label_training = video_training['img'].tolist()
	aq_label = aquarium_training['img'].tolist()
	cyber_label = cyber_training['img'].tolist()
	insta_label_training = insta_training['img'].tolist()
	server_label_test = server_test['img'].tolist()
	insta_label_test = insta_test['img'].tolist()
	draw_label_training = drawing_training['img'].tolist()
	draw_label_test = drawing_test['img'].tolist()
	not_shark_label_training = not_shark_training['img'].tolist()
	not_shark_label_test = not_shark_test['img'].tolist()

	for i in range(len(server_training)):
		label = server_label_training[i]
		try:
			shutil.move(class_2_training + label, server_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(video_training)):
		label = video_label_training[i]
		try:
			shutil.move(class_2_training + label, video_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(aquarium_training)):
		label = aq_label[i]
		try:
			shutil.move(class_2_training + label, aq_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(cyber_training)):
		label = cyber_label[i]
		try:
			shutil.move(class_2_training + label, cyber_dir + label)
		except FileNotFoundError:
			continue

	insta_label_training = insta_training['img'].tolist()
	for i in range(len(insta_training)):
		label = insta_label_training[i]
		try:
			shutil.move(class_2_training + label, insta_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(server_test)):
		label = server_label_test[i]
		try:
			shutil.move(class_2_test + label, server_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(insta_test)):
		label = insta_label_test[i]
		try:
			shutil.move(class_2_test + label, insta_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(drawing_training)):
		label = draw_label_training[i]
		try:
			shutil.move(class_0_training + label, drawing_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(drawing_test)):
		label = draw_label_test[i]
		try:
			shutil.move(class_0_test + label, drawing_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(not_shark_training)):
		label = not_shark_label_training[i]
		try:
			shutil.move(class_1_training + label, not_shark_dir + label)
		except FileNotFoundError:
			continue

	for i in range(len(not_shark_test)):
		label = not_shark_label_test[i]
		try:
			shutil.move(class_1_test + label, not_shark_dir + label)
		except FileNotFoundError:
			continue
	print('DONE\n')