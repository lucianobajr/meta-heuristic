package export

import (
	"fmt"
	"image/color"
	"log"
	usecases "meta-heuristic/app/use-cases"
	"os"
	"path/filepath"
	"strconv"

	"github.com/olekukonko/tablewriter"
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
)

func table(results []float64) {
	// Criar uma nova tabela
	table := tablewriter.NewWriter(os.Stdout)
	table.SetHeader([]string{"Média", "Mínimo", "Máximo", "Desvio Padrão"})

	// Adicionar uma linha com as métricas
	table.Append([]string{
		formatFloat(usecases.Mean(results)),
		formatFloat(usecases.Min(results)),
		formatFloat(usecases.Max(results)),
		formatFloat(usecases.StandardDeviation(results)),
	})

	// Renderizar a tabela
	table.Render()
}

func formatFloat(value float64) string {
	return strconv.FormatFloat(value, 'f', 2, 64)
}

func generateBoxPlot(results []float64) error {
	// Criar o plot
	p := plot.New()

	// Configurar o título do plot
	p.Title.Text = "Boxplot dos Resultados"

	// Configurar os rótulos dos eixos
	p.X.Label.Text = "Resultados"
	p.Y.Label.Text = ""

	// Configurar os valores dos eixos
	pts := make(plotter.Values, len(results))
	for i, r := range results {
		pts[i] = r
	}

	// Calcular as estatísticas para o boxplot
	box, err := plotter.NewBoxPlot(vg.Points(20), 0.0, pts)

	if err != nil {
		log.Fatal(err)
	}

	box.FillColor = color.RGBA{R: 50, G: 150, B: 255, A: 255}
	box.Width = vg.Length(40)

	// Adicionar o boxplot ao plot
	p.Add(box)

	// Exportar a imagem para a pasta "out"
	outDir := "out"
	err = os.MkdirAll(outDir, os.ModePerm)
	if err != nil {
		return fmt.Errorf("erro ao criar a pasta de saída: %v", err)
	}

	outFile := filepath.Join(outDir, "boxplot.png")
	err = p.Save(10*vg.Inch, 6*vg.Inch, outFile)
	if err != nil {
		return fmt.Errorf("erro ao exportar a imagem: %v", err)
	}

	log.Printf("Boxplot gerado e exportado para %s\n", outFile)
	return nil
}

func Export(metrics *usecases.MetricsService) {
	result := metrics.GetMetrics()

	table(result.Results)
	generateBoxPlot(result.Results)
}
