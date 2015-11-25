// play_test
package mp

import (
	"testing"
)

func TestOps(t *testing.T) {
	err := Play("http://music.163.com/12331", "MP3")
	if err == nil {
		t.Error("Play() failed")		
	}
}