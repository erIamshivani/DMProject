library(shiny)
library(beeswarm)
library(shinythemes)
library(reticulate)

Dataset=read.csv('C:/Users/Shivanii/Desktop/DM/BreadBasket.csv')

ui <- fluidPage(
  theme = shinytheme("darkly"),
  includeCSS('C:/Users/Shivanii/Desktop/DM/style.css'),
  
 
  headerPanel("Transactions of a Bakery", windowTitle = "Data Mining and Warehousing mini project"),
  
  sidebarLayout(
    
    sidebarPanel(
      
      width=4,
      h3("Choose anyone plot:"),
      br(),
      tabsetPanel
      (
        id = "tabset",
        type="pills",
        tabPanel("Count Plot"),
        tabPanel("Swarm Plot"),
        
      ),
      br(),
      br(),
      actionButton("go", "Plot graph"),
      br(),
      br(),
      tags$div(class="header", checked=NA,
               tags$h4("For entire project details and documents "),
               tags$a(href="https://www.google.com", "Click Here!")
    )
    ),
    mainPanel(
      plotOutput("plot")
    )
  
)
)

server <- function(input, output){
  v <- reactiveValues(doPlot = FALSE)
  
  observeEvent(input$go, {
    # 0 will be coerced to FALSE
    # 1+ will be coerced to TRUE
    v$doPlot <- input$go
  })
  
  observeEvent(input$tabset, {
    v$doPlot <- FALSE
  })  
  
  output$plot <- renderPlot({
    if (v$doPlot == FALSE) return()
    
    isolate({
      data <- if (input$tabset == "Count Plot") {
        
        
        
        counts <- table(Dataset$Class)
        barplot(counts, main="Count plot", 
                xlab="Classes",col = "#0b3e91")
        
      } else {
        
        beeswarm(Time~Item, data = Dataset, 
                 log = TRUE, pch = 16, col = rainbow(8),
                 main = 'Swarm')
      }
      
    })
  })
}

shinyApp(ui, server)
