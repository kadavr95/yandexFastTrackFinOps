package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Feed map[string]string

type Product struct {
	OfferId   string `json:"offer_id"`
	MarketSku string `json:"market_sku"`
	Price     int    `json:"price"`
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	linesS, err := reader.ReadString('\n')
	if err != nil {
		panic(err)
	}
	lines, err := strconv.Atoi(strings.TrimSpace(linesS))
	if err != nil {
		panic(err)
	}

	for i := 0; i < lines; i++ {
		linesS, _ := reader.ReadString('\n')
		fmt.Println(linesS)
	}
	fmt.Println(lines)

}
