from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class LinuxCommand(BaseModel):
	command: str
	description: str


in_memory_datastore = [
	LinuxCommand(command="pwd", description="find out the path of the current working directory"),
	LinuxCommand(command="cd", description="navigate through the Linux files and directories"),
	LinuxCommand(command="cat", description="used to list the contents of a file on the standard output"),
	LinuxCommand(command="cp", description="copy files from the current directory to a different directory"),
	LinuxCommand(command="mv", description="move files / rename files"),
	LinuxCommand(command="mkdir", description="make a new directory"),
	LinuxCommand(command="rmdir", description="delete a directory"),
	LinuxCommand(command="rm", description="delete directories and the contents within them"),
	LinuxCommand(command="touch", description="create a blank new file through the Linux command line"),
	LinuxCommand(command="locate", description="locate a file, just like the search command in Windows"),
	LinuxCommand(command="find", description="locate files within a given directory"),
	LinuxCommand(command="grep", description="search through all the text in a given file"),
	LinuxCommand(command="sudo", description="this command enables you to perform tasks that require administrative "
	                                         "or root permissions"),
	LinuxCommand(command="df", description="get a report on the system’s disk space usage"),
	LinuxCommand(command="du", description="check how much space a file or a directory takes"),
	LinuxCommand(command="head", description="used to view the first lines of any text file"),
	LinuxCommand(command="tail", description="the tail command will display the last ten lines of a text file"),
	LinuxCommand(command="diff", description="compares the contents of two files line by line"),
	LinuxCommand(command="tar", description="the most used command to archive multiple files into a tarball"),
	LinuxCommand(command="chmod", description="used to change the read, write, and execute permissions of files and "
	                                          "directories"),
	LinuxCommand(command="chown", description="enables you to change or transfer the ownership of a file to the "
	                                          "specified username"),
	LinuxCommand(command="jobs", description="will display all current jobs along with their statuses"),
	LinuxCommand(command="kill", description="send a certain signal to the misbehaving app and instructs the app to "
	                                         "terminate itself"),
	LinuxCommand(command="ping", description="check your connectivity status to a server"),
	LinuxCommand(command="wget", description="download files from the internet")

]


@app.get('/linux_commands')
def get_linux_commands():
	return {"Linux_Commands": in_memory_datastore}


@app.get('/linux_commands/{command_id}')
def get_programming_language(command_id: int):
	return in_memory_datastore[command_id]


@app.put('/linux_commands/{command_id}')
async def update_linux_command(command_id: int, updated_linux_command: LinuxCommand):
	in_memory_datastore[command_id] = updated_linux_command
	return updated_linux_command


@app.delete('/linux_commands/{command_id}')
async def delete_linux_command(command_id: int):
	del in_memory_datastore[command_id]
