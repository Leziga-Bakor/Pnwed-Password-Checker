import requests
import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    try:
        res = requests.get(url)
    except:
        showerror('Connection Error', 'Please check your internet connection and try again')
    else:
        if res.status_code != 200:
            raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
        return res


def get_password_leaks_count(response, hash_to_check):
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:

        if h == hash_to_check:
            return count
    return 0


def check_pwned_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, rest = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, rest)


def main(args):
    for password in args:
        count = check_pwned_api(password)
        if count:
            password1 = password[0] + 4 * 'x' + password[-1]
            showinfo('Process Completed',
                     f"{password1} was found {count} times... you should consider changing your password")
        else:
            showinfo('Process Completed', f'{password1} was NOT found. Your pass word has not been pwned. Carry on!')
    return "done!"


def show_hide_psd():
    if check_var.get():
        ttk.Entry(win, show='', width=100, textvariable=pas).grid(column=0, row=1)

    else:
        ttk.Entry(win, show='*', width=100, textvariable=pas).grid(column=0, row=1)


if __name__ == '__main__':

    win = tk.Tk()

    win.attributes('-topmost', True)
    win.title('Password Checker')
    ttk.Label(win, text='Enter passwords seperated by space: ').grid(column=0, row=0)



    def click():
        passwords = pas.get().split()
        if passwords:
            main(passwords)
        else:
            showinfo("Process Completed", "No passwords Entered")
        win.quit()


    pas = tk.StringVar()
    ttk.Entry(win, show='*', width=100, textvariable=pas).grid(column=0, row=1)  # Button widget

    check_var = tk.IntVar()
    ttk.Checkbutton(win, text="Show password", variable=check_var, onvalue=1, offvalue=0,
                    command=show_hide_psd).grid(column=1, row=1)

    ttk.Button(win, text="submit", command=click).grid(column=2, row=1)

    win.mainloop()




