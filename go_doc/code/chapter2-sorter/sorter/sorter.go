// sorter
// main program
// 1. parse the input from terminal
// 2. read data from input file
// 3. call the correspond sort function
// 4. write the sort result to output file
// 5. print the cost time

package main

import (
	"fmt";
	"flag";		// parse the command input
	
	"bufio";		// read data from input file
	"io";
	"os";
	"strconv";
				
	"algorithm/bubblesort";	// algorithm
	"algorithm/qsort";
)

var infile *string = flag.String("i", "infile", "File contains values for sorting")
var outfile *string = flag.String("o", "outfile", "File to receive sorted values")
var algorithm *string = flag.String("a", "qsort", "Sort algorithm")

func readValues(infile string) (values []int, err error) {
	file, err := os.Open(infile)
	if err != nil {
		fmt.Println("Failed to open the input file ", infile)
		return 
	}
	defer file.Close()
	
	br := bufio.NewReader(file)
	
	values = make([]int, 0)
	for {
		line, isPrefix, err1 := br.ReadLine()

				if err1 != nil {
			if err1 != io.EOF {
				err = err1
			}
			break
		}
		if isPrefix {
			fmt.Println("A too long line, seems unexpected.")
			return 
		}
		
		str := string(line) // translate array chars to string
		
		value, err1 := strconv.Atoi(str)
		if err1 != nil {
			err = err1
			return 
		}
		values = append(values, value)
	}	
	return 
}

func writeValues(values []int, outfile string) error {
	file, err := os.Create(outfile)
	if err != nil {
		fmt.Println("Failed to create the output file ", outfile)
		return err
	}
	defer file.Close()
	
	for _, value := range values {
		str := strconv.Itoa(value)
		file.WriteString(str + "\n")
	}
	
	return nil
}

func main() {
	flag.Parse()
	
	if infile != nil {
		fmt.Println("infile = ", *infile, "outfile = ", *outfile, "algorithm = ", *algorithm)
	}
	
	values, err := readValues(*infile)
	if err == nil {
		t1 := time.Now()
		switch *algorithm {
			case "qsort":
				qsort.QuickSort(values)
			case "bubblesort":
				bubblesort.BubbleSort(values)
			default:
				fmt.Println("Sorting algorithm ", *algorithm, " is either unknow or unsuppected.")
		}
		t2 := time.Now()
		
		fmt.Println("The sorting process costs ", t2.Sub(t1), " to complete.")
		
		writeValues(values)
		
	} else {
		fmt.Println(err)	
	}
}
