// mp3
package mp

import (
	"fmt";
	"time"
)

type MP3Player struct {
	stat int
	progress int
}

func NewMP3Player() *MP3Player {
	return &MP3Player{}
}

func (p *MP3Player)Play(source string) (err error) {
	fmt.Println("Playering MP3 music, ", source)
	p.progress = 0
	
	for p.progress <= 100 {
		time.Sleep(100 * time.Millisecond)
		fmt.Print(".")
		p.progress += 10
	}
	
	fmt.Println("\nFinished playeing ", source)
	
	return nil
}