// manager
package library

import (
	"errors";
)

type MusicEntry struct {
	Id string
	Name string
	Artist string
	Source string
	Type string
}

type MusicManager struct {
	musics []MusicEntry
}

func NewMusicManager() *MusicManager {
	return &MusicManager{make([]MusicEntry, 0)}
}

func (m *MusicManager) Len() int {
	return len(m.musics)
}

func (m *MusicManager) Get(index int) (music *MusicEntry, err error) {
	if index < 0 || index >= len(m.musics) {
		return nil, errors.New("Index out of range.")
	}
	return &m.musics[index], nil
}

func (m *MusicManager) Find(name string) *MusicEntry {
	if len(m.musics) == 0 {
		return nil
	}
	
	for _, m := range m.musics {
		if m.Name == name {
			return &m
		}
	}
	return nil
}

func (m *MusicManager) Add(music *MusicEntry) {
	m.musics = append(m.musics, *music)
}

func (m *MusicManager) Remove(index int) *MusicEntry {
	if index < 0 || index >= len(m.musics) {
		return nil
	}
	
	removeMusic := &m.musics[index]
	
	// delete from slice
	if index < len(m.musics)-1 { // mid one
		m.musics = append(m.musics[:index-1], m.musics[index+1:]...)
	} else if index == 0 { 		// the only one
		m.musics = make([]MusicEntry, 0)
	} else { 					// last one
		m.musics = m.musics[:index-1]
	}
	
	return removeMusic
}

func (m *MusicManager) RemoveByName(name string) (music *MusicEntry, err error) {

	if len(m.musics) == 0 {
		return nil, errors.New("music list is empty")
	}
	
	i := 0
	for ; i < len(m.musics); i++ {
		if m.musics[i].Name == name {
			break 
		}
	}
	
	if i >= len(m.musics) {
		return nil, errors.New("Cannot find")
	}
		
	mu := m.Remove(i)
	if mu == nil {
		return nil, errors.New("Cannot find ")
	}
	
	return mu, nil
}













