// play
package mp

import (
	"fmt";
	"errors"
)

type Player interface {
	Play(source string) (err error)
}

func Play(source, mtype string) (err error) {
	var p Player
	
	switch mtype {
		case "MP3":
			p = NewMP3Player()
		//case "WAV":
		//	p = &WAVPlayer()
		default:
			fmt.Println("Unsupported music type ", mtype)
			return errors.New("Unsupported music type")
	}
	
	err1 := p.Play(source)
	return err1
}
