package main
import (
	"log"
	"fmt"
	"net/http"
)
func sayHello(w http.ResponseWriter, r *http.Request) {
	// parse request
	r.ParseForm()
	fmt.Println("request form: ", r.Form)
	fmt.Print("request url: ", r.URL.Path)
	fmt.Println("request scheme: ", r.URL.Scheme)
	fmt.Println(r.Form["url_long"])
	for k, v := range r.Form {
		fmt.Println("key: ", k)
		fmt.Println("val: ", v)
	}
	fmt.Fprintf(w, "helllllo!!! this is from Siren!!!")
}
func main() {
	fmt.Println("hello, Go lang.")
	http.HandleFunc("/", sayHello)
	err := http.ListenAndServe(":9000", nil)
	if err != nil {
		log.Fatal("Listen and serve: ", err)
	}
}