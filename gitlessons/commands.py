GIT -   распределенная система котнтроля версий это система  для отслеживания и ведения истории изменений в ваших файлов или проекта


репозиторий - это хранилище ваших файлов, которые вы отслеживаете при помощи ГИТа и их  изменений 


команды GIT:
	1 git init - она создает новый гит репозиторий локально на вашем ПК, создаст она в той директории где вы запускаете эту команду
	2  git add - когда мы создаем и изменяем файлы, то при помощи этой команды мы загружаем все изменения в промежуточное место хранение
	git add <file_name>
	git add . - все в текущей директории
	3 git commit - как только мы достигаем определенного момента в разработке то мы фиксируем в репозитории и добавляем комментарии
	git commit -m '<comment>'
	.
	4 git remote add - команда для того, чтобы связзать ваш локальный репозиторий с удаленым репозиторием (репо в гитхабе)
	git remote add <название подкючения> <ссылка на репозиторий>
	git remote add origin <url>
	5 git push - после коммита изменений при помощи этой команды мы отправляем наши изменения в файлах на удаленый репозиторий 
	git push <origin> <название ветки (main)>
	git push origin main
	
-------------------------------------------------------------------------------
git init 
git branch -M main - переименовывает ветку с мастера на мэйн
git add .
git commit -n 'коммент' (все дабвлено в локальный репозиторий)
git remote add origin <url>
git push origin main
////////////////////////////////////////
git add
git commit -m 'comment'
git push origin main
