from process_files import getDF_A as getDF
import pandas as pd

def main():
    df = getDF()
    # print(df)
    # df = df[df['Category'] == 'Inside metropolitan statistical areas' | df['Category'] == 'Inside principal cities']
    #             # 'Inside principal cities',
    #             # 'Outside principal cities',
    #             # 'Outside metropolitan statistical areas']]
    # print(df)

if __name__ == '__main__':
    main()