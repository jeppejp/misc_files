#include <linux/input.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>

int main(int argc, char **argv)
{
    int fd_mouse; // event0
    int fd_keyboard; // event1
    fd_mouse = open("/dev/input/event0", O_RDONLY);
    fd_keyboard = open("/dev/input/event1", O_RDONLY);
    struct input_event ev;
    struct timeval tv;

    fd_set rfds;

    int rres;
    tv.tv_sec = 1;
    tv.tv_usec = 500000;

    int state = 1;
    int last_state = 0;
    time_t last_active = time(NULL);

    while (1)
    {
    FD_ZERO(&rfds);
    FD_SET(fd_mouse, &rfds);
    FD_SET(fd_keyboard, &rfds);


        int res = select(fd_keyboard+1, &rfds, NULL, NULL, &tv);

        if(res == -1)
            perror("select()");
        else if(res)
        {
            printf("res\n");
            if(FD_ISSET(fd_mouse,&rfds))
            {
                printf("mouse\n");
                rres = read(fd_mouse, &ev, sizeof(ev));
                last_active = time(NULL);
                state = 1;
            }
            if(FD_ISSET(fd_keyboard, &rfds))
            {
                printf("keyboard\n");
                rres = read(fd_keyboard, &ev, sizeof(ev));
                last_active = time(NULL);
                state = 1;

            }
        }else{
            printf("nothing: inactive for %d\n", time(NULL)-last_active);
    tv.tv_sec = 1;
    tv.tv_usec = 500000;
            if ((time(NULL)-last_active) > 3)
            {
                state = 0;
            }
        }

        if (state != last_state)
        {
            last_state = state;
            printf("state is now %d\n", state);


        }

    }
}
