using Pglet;
using Pglet.Controls;
using System;
using System.Threading.Tasks;

namespace StackExample
{
    class Program
    {
        static async Task Main()
        {
            await PgletClient.ServeApp(async (page) =>
            {
                await page.AddAsync(
                    new Text { Value = "Vertical stack", Size = TextSize.Large },
                    new Stack
                    {
                        Controls = {
                            new Text { Value = "Text 1" },
                            new Text { Value = "Text 2" }
                        }
                    },
                    new Text { Value = "Horizontal stack", Size = TextSize.Large },
                    new Stack
                    {
                        Horizontal = true,
                        Controls = {
                            new Text { Value = "Text 1" },
                            new Text { Value = "Text 2" }
                        }
                    });


            }, "csharp-stack");
        }
    }
}
