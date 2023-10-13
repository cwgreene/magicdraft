mkdir -p data
if ! [ -f ./data/AllPrintings.json ]; then
    if ! [ -f ./data/AllPrintings.json.bz2 ]; then
        curl 'https://mtgjson.com/api/v5/AllPrintings.json.bz2' --output 'src/magicdraft/data/AllPrintings.json.bz2'
    fi
    echo "Bunzipping AllPrintings"
    cd data
    bunzip2 ./AllPrintings.json.bz2
fi
echo "Data Acquired"
