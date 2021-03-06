from package import (
    do_news,do_quote,do_movie,do_youtube,do_wallpaper,do_crypto,login,do_insta
)



#app = Flask(__name__)
import cmd
import sys
#flask web
#@app.route("/")
class FirstCmdApplication(cmd.Cmd):
    try:
        intro = "Welcome {username}!".format(username=sys.argv[1])


    except IndexError:
        print("Please provide your username!")
        #exit()
        user = input("Enter username :")
        intro = "Welcome {username}!".format(username=user)

    from termcolor import colored
    intr = """
                    --------------------------------------------------------------------------------------------------
                    \t\t\t\t Welcome to Cli Application


                    \t *.news : for News
                    \t *.quote : for quote of the day
                    \t *.wallpaper : to display wallpaper
                    \t *.youtube video download : download a Video
                    \t *.movie title_movie : for Movie details
                    \t *.crypto: for Crypto Currency prices
                    \t *.login : facebook and instagram login via CMD
                    \t *.wiki : execute wikipedia search
                    \t *.exit
                    \t\t\t\t\t\t\t\t\t for help type help 
                    """

    intri = colored(intr, 'yellow')
    print(intri)



    prompt = 'Command: '

    def do_intro(self,arg):
        from termcolor import colored
        "display the options"
        intr = """
                            --------------------------------------------------------------------------------------------------
                            \t\t\t\t Welcome to Cli Application


                            \t *.news : for News
                            \t *.quote : for quote of the day
                            \t *.wallpaper : to display wallpaper
                            \t *.youtube video download : download a Video
                            \t *.movie title_movie : for Movie details
                            \t *.crypto: for Crypto Currency prices
                            \t *.login : facebook login via CMD
                            \t *.exit
                            \t\t\t\t\t\t\t\t\t for help type help 
                            """

        intrc = colored(intr, 'yellow')
        print(intrc)

    def do_login(self,arg):
        "facbook login via selenium"
        choice =input("press 1 for facebook login \npress 2 for instagram login\n")
        if(choice=='1'):
            login()
        elif (choice=='2'):
            do_insta()


    def do_youtube(self,arg):
        "youtube video"
        do_youtube()

    def do_wiki(self,arg):
        "execute wikipedia search"

    def do_crypto(self,arg):
        "crypto currency price"
        do_crypto()

    def do_history(self, arg):
        "not working"
        print(self._history)

    def do_news(self, arg):
        "Read today's news"
        do_news()

    def do_movie(self,title):
        "get movies ratings n info"
        do_movie(title)

    def do_quote(self, arg):
        "Read quote of the day"
        do_quote()
    def do_wallpaper(self,arg):
        "Display Wallpaper"
        do_wallpaper()



    def do_exit(self, arg):
        "Exit the application"
        return -1

    def precmd(self, line):
        """ This method is called after the input but before
            it has been interpreted. If you want to modify the input line
            before execution (for example, variable substitution) do it here.
        """
        if line != '':
            self._history += [ line.strip() ]
        return line

    def postcmd(self, stop, line):
        """If you want to stop the console, return something that evaluates to true.
           If you want to do some post command processing, do it here.
        """
        return stop


    def preloop(self):
        "Initialization before prompting user for commands"
        cmd.Cmd.preloop(self)


        self._history = []

    def postloop(self):
        "Take care of any unfinished business."
        print("Exiting...")
        cmd.Cmd.postloop(self)



if __name__=='__main__':

    FirstCmdApplication().cmdloop()
