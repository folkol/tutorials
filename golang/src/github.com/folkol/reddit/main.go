package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Item struct {
	Title string
	URL   string
}

type Response struct {
	Data struct {
		Children []struct {
			Data Item
		}
	}
}

func main() {
	client := &http.Client{}
	req, err := http.NewRequest("GET", "http://reddit.com/r/golang.json", nil)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Add("User-Agent", "folkol.com google tutorial bot")
	resp, err := client.Do(req)
	if resp.StatusCode != http.StatusOK {
		log.Fatal(resp.Status)
	}
	r := new(Response)
	err = json.NewDecoder(resp.Body).Decode(r)
	if err != nil {
		log.Fatal(err)
	}
	for _, child := range r.Data.Children {
		fmt.Println(child.Data.Title)
	}
}
