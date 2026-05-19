import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mpl


def generate_graph(incidents):

    
    mpl.rcParams.update(mpl.rcParamsDefault)

    severity_map = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "CRITICAL": 4
    }

    colors = {
        "CRITICAL": "#F4A6A6",
        "HIGH": "#F7C59F",
        "MEDIUM": "#FAEDCB",
        "LOW": "#B8F2E6"
    }

    x, y, c, labels = [], [], [], []

    for i, inc in enumerate(incidents):
        x.append(i)
        y.append(severity_map[inc["severity"]])
        c.append(colors[inc["severity"]])
        labels.append(f"{inc['issue']} ({inc['count']})")

    plt.figure(figsize=(12, 6))

    plt.xlim(-0.5, len(x) - 0.5)

   
    plt.axhspan(0.5, 1.5, color="#B8F2E6", alpha=0.1)
    plt.axhspan(1.5, 2.5, color="#FAEDCB", alpha=0.1)
    plt.axhspan(2.5, 3.5, color="#F7C59F", alpha=0.1)
    plt.axhspan(3.5, 4.5, color="#F4A6A6", alpha=0.1)

    
    plt.plot(
        x, y,
        linestyle='-',
        color='black',
        alpha=0.6,
        zorder=1
    )

    
    plt.scatter(
        x, y,
        s=250,
        c=c,
        edgecolors='none',
        linewidths=0,
        zorder=3
    )

   
    # labels 
    for i, label in enumerate(labels): 
        plt.text(x[i], y[i] + 0.08, label, fontsize=9, ha='center')
    

    plt.xlabel("Time (Incident Order)")
    plt.ylabel("Severity")

    plt.yticks([1, 2, 3, 4])
    plt.gca().set_yticklabels(["LOW", "MEDIUM", "HIGH", "CRITICAL"])

    plt.title("Incident Timeline vs Severity")

    legend_patches = [
        mpatches.Patch(color="#F4A6A6", label="CRITICAL"),
        mpatches.Patch(color="#F7C59F", label="HIGH"),
        mpatches.Patch(color="#FAEDCB", label="MEDIUM"),
        mpatches.Patch(color="#B8F2E6", label="LOW"),
    ]

    plt.legend(handles=legend_patches, loc="upper left")
    plt.grid(True, linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.show()