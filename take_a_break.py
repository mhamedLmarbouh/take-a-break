import webbrowser
import time
import argparse
from validator import url as validate_url

"""
this scripte remind you to take a break by opening a url that you provide 
in a interval and as many time as you want.
example; take_a_break.py -t 45 -u min -bn 3 --url https://www.youtube.com/watch?v=uXRLanZp2sk
"""

def main():
    parser = setup_parser()

    parsed = parser.parse_args()

    break_url= parsed.url
    while not validate_url(break_url):
        print('Invalide url')
        break_url=input('entre your break url: ')

    sleep_time = set_sleep_time(parsed.time,parsed.unit)

    breaks_counter=0
    while breaks_counter < parsed.breaks:
        time.sleep(sleep_time)
        print('take a break')
        webbrowser.open(break_url)  
        breaks_counter+=1
    
    print('Done!')


def set_sleep_time(time=20,unit='min'):
    """
    this methode return break time in seconds 
    """
    if unit=='h':
        return int(time)*60*60
    elif unit=='min':
        return int(time)*60
    elif unit=='sec':
        return int(time)
    else:
        print('Expecting h, min or sec after {} but find {}'.format(time,unit))
        exit()

def setup_parser():
    """
    this methose setup the argparser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--time',
        default=20,
        help='time between two breaks',
        type=int
    )
    parser.add_argument(
        '-u',
        '--unit',
        default='min',
        help='time unit default is \'min\' other options are \'sec\' and \'h\' ',
        type=str
    )
    parser.add_argument(
        '-b',
        '--breaks',
        default=1,
        help='number of breaks to take default is 1 ',
        type=int
    )
    parser.add_argument(
        '--url',
        required=True,
        help='number of breaks to take default is 1 ',
        type=str
    )
    return parser

if __name__ == "__main__":
    main()
