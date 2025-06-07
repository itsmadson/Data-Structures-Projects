import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularPlaylist:
    def __init__(self):
        self.head = None
        self.current = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.current = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
        
        self.size += 1
        return new_node

    def remove(self, node):
        if not node or self.size == 0:
            return None
        
        if self.size == 1:
            self.head = None
            self.current = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            if node == self.head:
                self.head = node.next
            if node == self.current:
                self.current = node.next

        self.size -= 1
        return node.data

    def next_song(self):
        if self.current:
            self.current = self.current.next
            return self.current.data

    def prev_song(self):
        if self.current:
            self.current = self.current.prev
            return self.current.data

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        
        pygame.mixer.init()
        self.playlist = CircularPlaylist()
        
        self.song_nodes = {}
        self.is_playing = False
        self.is_paused = False
        
        self.create_ui()

    def setup_window(self):
        self.root.title("Music Player")
        self.root.geometry("400x400")
        self.root.configure(bg='#121212')
        self.root.resizable(False, False)

    def create_ui(self):
        # main container
        main_container = tk.Frame(self.root, bg='#121212')
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # file info
        top_frame = tk.Frame(main_container, bg='#121212')
        top_frame.pack(fill=tk.X)

        # current file 
        self.current_song_label = tk.Label(
            top_frame, 
            text="No Song Selected", 
            font=('Arial', 12), 
            bg='#121212', 
            fg='#FFFFFF',
            anchor='w'
        )
        self.current_song_label.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # add btn
        add_btn = tk.Button(
            top_frame, 
            text="Add +", 
            command=self.add_songs, 
            bg='#ff8fab',
            fg='#FFFFFF',
            font=('Arial', 10, 'bold'),
            width=3
        )
        add_btn.pack(side=tk.RIGHT, padx=5)

        # playlist frame
        playlist_frame = tk.Frame(main_container, bg='#1E1E1E')
        playlist_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        
        self.song_listbox = tk.Listbox(
            playlist_frame, 
            bg='#1E1E1E', 
            fg='#FFFFFF', 
            selectbackground='#ff8fab', 
            selectforeground='#FFFFFF',
            font=('Arial', 10),
            borderwidth=0, 
            highlightthickness=0
        )
        self.song_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

      
        control_frame = tk.Frame(main_container, bg='#121212')
        control_frame.pack(fill=tk.X, pady=5)

        # prev btn
        prev_btn = tk.Button(
            control_frame, 
            text="◀", 
            command=self.play_previous, 
            bg='#1E1E1E',
            fg='#FFFFFF',
            font=('Arial', 12, 'bold'),
            width=3
        )
        prev_btn.pack(side=tk.LEFT, expand=True)

        # play/pause btn
        self.play_pause_btn = tk.Button(
            control_frame, 
            text="►", 
            command=self.toggle_play_pause, 
            bg='#ff8fab',
            fg='#FFFFFF',
            font=('Arial', 12, 'bold'),
            width=3
        )
        self.play_pause_btn.pack(side=tk.LEFT, expand=True)

        # next btn
        next_btn = tk.Button(
            control_frame, 
            text="▶", 
            command=self.play_next, 
            bg='#1E1E1E',
            fg='#FFFFFF',
            font=('Arial', 12, 'bold'),
            width=3
        )
        next_btn.pack(side=tk.LEFT, expand=True)

        # remove btn
        remove_btn = tk.Button(
            control_frame, 
            text="✖", 
            command=self.remove_song, 
            bg='#B22222',
            fg='#FFFFFF',
            font=('Arial', 12, 'bold'),
            width=3
        )
        remove_btn.pack(side=tk.LEFT, expand=True)

    def add_songs(self):
        songs = filedialog.askopenfilenames(
            initialdir='/', 
            title="Choose Songs", 
            filetypes=[("MP3 Files", "*.mp3")]
        )

        for song_path in songs:
            song_name = os.path.basename(song_path)
            
            if song_name in self.song_nodes:
                continue

            self.song_listbox.insert(tk.END, song_name)
            
            node = self.playlist.append(song_path)
            self.song_nodes[song_name] = node

    def remove_song(self):
        try:
            selection = self.song_listbox.curselection()[0]
            song_name = self.song_listbox.get(selection)
            
            self.song_listbox.delete(selection)
            
            if song_name in self.song_nodes:
                node = self.song_nodes[song_name]
                self.playlist.remove(node)
                del self.song_nodes[song_name]
                
            if not self.playlist.size:
                pygame.mixer.music.stop()
                self.current_song_label.config(text="No Song Selected")
                self.play_pause_btn.config(text="►")
                self.is_playing = False
                self.is_paused = False
        except IndexError:
            messagebox.showinfo("Remove Song", "Please select a song to remove")

    def toggle_play_pause(self):
        if self.playlist.size == 0:
            return

        if not self.is_playing and not self.is_paused:
            current_song = self.playlist.current.data
            self.play_song(current_song)
            self.play_pause_btn.config(text="❚❚", bg='#ffc2d1')
        elif self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.is_paused = True
            self.play_pause_btn.config(text="►", bg='#ff8fab')
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.is_paused = False
            self.play_pause_btn.config(text="❚❚", bg='#ffc2d1')

    def play_song(self, song_path):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

            self.is_playing = True
            self.is_paused = False
            self.play_pause_btn.config(text="❚❚", bg='#9c1616')

            song_name = os.path.basename(song_path)
            self.current_song_label.config(text=song_name)
        except Exception as e:
            messagebox.showerror("Playback Error", f"Could not play song: {e}")

    def play_next(self):
        if self.playlist.size == 0:
            return

        next_song = self.playlist.next_song()
        self.play_song(next_song)   
        next_song_name = os.path.basename(next_song)
        for i in range(self.song_listbox.size()):
            if self.song_listbox.get(i) == next_song_name:
                self.song_listbox.selection_clear(0, tk.END)
                self.song_listbox.selection_set(i)
                self.song_listbox.activate(i)
                break

    def play_previous(self):
        if self.playlist.size == 0:
            return

        prev_song = self.playlist.prev_song()
        self.play_song(prev_song)
        
        prev_song_name = os.path.basename(prev_song)
        for i in range(self.song_listbox.size()):
            if self.song_listbox.get(i) == prev_song_name:
                self.song_listbox.selection_clear(0, tk.END)
                self.song_listbox.selection_set(i)
                self.song_listbox.activate(i)
                break

def main():
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()