class Song {
  name;
  nextSong;
  
  constructor(name) {
    this.name = name;
  }
  
  /**
   * @return {boolean} true if the playlist is repeating, false if not.
   */
  isRepeatingPlaylist() {
    const playedSongs = new Set();
    let song = this;

    while(song) {
      if (playedSongs.has(song.name)) {
        return true;
      }
      playedSongs.add(song.name);
      song = song.nextSong || null;
    }
    return false;
  }
}

let first = new Song("Hello");
let second = new Song("Eye of the tiger");
let third = new Song("Roar");

first.nextSong = second;
second.nextSong = third;

console.log(first.isRepeatingPlaylist());