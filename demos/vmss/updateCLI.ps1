az vmss extension set `
  --publisher Microsoft.Azure.Extensions `
  --version 2.0 `
  --name CustomScript `
  --resource-group 02tasks `
  --vmss-name vmss `
  --settings .\updateapp.json