using Pglet;
using Pglet.Controls;
using System;
using System.Threading.Tasks;

namespace ButtonsExample
{
    class Program
    {
        static async Task Main()
        {
            await PgletClient.ServeApp(async (page) =>
            {
                await page.AddAsync(
                    new Text { Value = "Standard button", Size = TextSize.Large },
                    new Stack
                    {
                        Horizontal = true,
                        Controls = {
                            new Button { Text = "Standard", OnClick = (e) =>
                            {
                                Console.WriteLine("Button clicked!");
                            }},
                            new Button { Text = "Standard disabled", Disabled = true }
                        }
                    },
                    new Text { Value = "Primary button", Size = TextSize.Large },
                    new Stack
                    {
                        Horizontal = true,
                        Controls = {
                            new Button { Primary = true, Text = "Primary" },
                            new Button { Primary = true, Text = "Primary disabled", Disabled = true }
                        }
                    },
                    new Text { Value = "Compound button", Size = TextSize.Large },
                    new Stack
                    {
                        Horizontal = true,
                        Controls = {
                            new Button { Compound = true, Text = "Compound", SecondaryText = "This is a secondary text"},
                            new Button { Compound = true, Primary = true, Text = "Primary Compound", SecondaryText = "This is a secondary text" }
                        }
                    });


            }, "csharp-buttons");
        }
    }
}
