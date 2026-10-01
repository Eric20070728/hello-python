import datetime
import time


def main():
    github_user = "Eric20070728"
    print(f"Hello, World! I am {github_user} on GitHub.")
    print(f"Today is {datetime.date.today()}.")

    print("\nStarting countdown:")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Done!")


if __name__ == "__main__":
    main()
