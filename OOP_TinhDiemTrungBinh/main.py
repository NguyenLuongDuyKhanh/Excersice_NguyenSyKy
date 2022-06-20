import csv


class BANGDIEM:
    def __init__(self, input_file, output_file):
        self.contain, self.header = self.load_dulieu(input_file)
        self.diemtrungbinh = self.tinhdiem_trungbinh()
        succeed = self.luudiem_trungbinh(output_file)
        if succeed:
            print("print ok")
        # print(self.contain)
        # print(self.header)

    # Phương thức load_dulieu: Load dữ liệu từ đường dẫn file vào một list.
    def load_dulieu(self, input_file):
        # import transcript file
        with open(input_file, "r") as f:
            contain = f.readlines()
            header = contain[0].strip().split(";")
        return contain, header

    # Phương thức tinhdiem_trungbinh: Chức năng tương tự như hàm tinhdiem_trungbinh
    # của assignment 2, input của phương thức tinhdiem_trungbinh
    # thay thế đường dẫn bảng điểm chi tiết bằng output của phương thức load_dulieu.

    def tinhdiem_trungbinh(self):
        result = {}
        for line in self.contain[1:]:
            if line.split(";")[0] not in result.keys():
                result[line.split(";")[0]] = {}

                for x in range(1, 9):
                    if len(line.split(";")[x].split(",")) == 4:
                        result[line.split(";")[0]][self.header[x]] = round(
                            sum(
                                [
                                    a * b
                                    for a, b in zip(
                                        map(float, line.split(";")[x].split(",")),
                                        [0.05, 0.1, 0.15, 0.7],
                                    )
                                ]
                            ),
                            2,
                        )
                    elif len(line.split(";")[x].split(",")) == 5:
                        result[line.split(";")[0]][self.header[x]] = round(
                            sum(
                                [
                                    a * b
                                    for a, b in zip(
                                        map(float, line.split(";")[x].split(",")),
                                        [0.05, 0.1, 0.1, 0.15, 0.6],
                                    )
                                ]
                            ),
                            2,
                        )

        return result

    # Phương thức luudiem_trungbinh: Chức năng tương tự như hàm luudiem_trungbinh của assignment 2
    def luudiem_trungbinh(self, outputfile):
        try:
            with open(outputfile, "w", newline="") as f:
                writer = csv.DictWriter(f, delimiter=";", fieldnames=self.header)
                writer.writeheader()
                for key in self.diemtrungbinh.keys():
                    writer.writerow(
                        {
                            "student_id": key,
                            "math": self.diemtrungbinh[key]["math"],
                            "physics": self.diemtrungbinh[key]["physics"],
                            "chemistry": self.diemtrungbinh[key]["chemistry"],
                            "biology": self.diemtrungbinh[key]["biology"],
                            "literature": self.diemtrungbinh[key]["literature"],
                            "english": self.diemtrungbinh[key]["english"],
                            "history": self.diemtrungbinh[key]["history"],
                            "geography": self.diemtrungbinh[key]["geography"],
                        }
                    )
            return True
        except:
            return False


class DANHGIA(BANGDIEM):
    def __init__(self, input_file, outputfile, outputA):
        super().__init__(input_file, outputfile)
        self.xeploai = self.xeploai_hocsinh()
        self.xeploai_daihoc = self.xeploai_thidaihoc_hocsinh()

        header = ["student_id", "grade", "[A,A1,B,C,D]"]
        with open(outputA, "w", newline="") as f:
            writer = csv.DictWriter(f, delimiter=";", fieldnames=header)
            writer.writeheader()
            for student in self.xeploai.keys():
                writer.writerow(
                    {
                        "student_id": student,
                        "grade": self.xeploai[student],
                        "[A,A1,B,C,D]": self.xeploai_daihoc[student],
                    }
                )

    # BANGDIEM(self):

    # Phương thức xeploai_hocsinh: Chức năng tương tự như hàm xeploai_hocsinh
    # của assignment 2. Input của phương thức xeploai_hocsinh
    # thay thế đường dẫn bảng điểm trung bình bằng output của phương thức
    # load_dulieu kế thừa từ class “BANGDIEM”.

    def xeploai_hocsinh(self):
        result = {}
        # print(self.diemtrungbinh)
        for student in self.diemtrungbinh.keys():
            # print(student)
            dtb_chuan = (
                (
                    float(self.diemtrungbinh[student]["math"])
                    + float(self.diemtrungbinh[student]["literature"])
                    + float(self.diemtrungbinh[student]["english"])
                )
                * 2
                + float(self.diemtrungbinh[student]["physics"])
                + float(self.diemtrungbinh[student]["chemistry"])
                + float(self.diemtrungbinh[student]["biology"])
                + float(self.diemtrungbinh[student]["history"])
                + float(self.diemtrungbinh[student]["geography"])
            ) / 11
            # print(dtb_chuan)
            diemso_list = [
                float(self.diemtrungbinh[student]["math"]),
                float(self.diemtrungbinh[student]["literature"]),
                float(self.diemtrungbinh[student]["english"]),
                float(self.diemtrungbinh[student]["physics"]),
                float(self.diemtrungbinh[student]["chemistry"]),
                float(self.diemtrungbinh[student]["biology"]),
                float(self.diemtrungbinh[student]["history"]),
                float(self.diemtrungbinh[student]["geography"]),
            ]

            if dtb_chuan > 9 and (True not in map(lambda x: x < 8, diemso_list)):
                result[student] = "Xuat sac"
            elif dtb_chuan > 8 and (True not in [map(lambda x: x < 6.5, diemso_list)]):
                result[student] = "Gioi"
            elif dtb_chuan > 6.5 and (True not in [map(lambda x: x < 5, diemso_list)]):
                result[student] = "Kha"
            elif dtb_chuan > 6 and (True not in [map(lambda x: x < 4.5, diemso_list)]):
                result[student] = "TB Kha"
            else:
                result[student] = "TB"
        print(result)
        return result

    # Phương thức xeploai_thidaihoc_hocsinh: Chức năng tương tự như hàm xeploai_thidaihoc_hocsinh
    # của assignment 2.

    def xeploai_thidaihoc_hocsinh(self):
        result = {}
        """
        {
        Kevin, [A, A1, B, C, D] 
        Harry, [A, A1, B, C, D]
        }
        """
        for student in self.diemtrungbinh.keys():
            result[student] = []
            A = (
                float(self.diemtrungbinh[student]["math"])
                + float(self.diemtrungbinh[student]["physics"])
                + float(self.diemtrungbinh[student]["chemistry"])
            )
            A1 = (
                float(self.diemtrungbinh[student]["math"])
                + float(self.diemtrungbinh[student]["physics"])
                + float(self.diemtrungbinh[student]["english"])
            )
            B = (
                float(self.diemtrungbinh[student]["math"])
                + float(self.diemtrungbinh[student]["chemistry"])
                + float(self.diemtrungbinh[student]["biology"])
            )
            C = (
                float(self.diemtrungbinh[student]["literature"])
                + float(self.diemtrungbinh[student]["history"])
                + float(self.diemtrungbinh[student]["geography"])
            )
            D = (
                float(self.diemtrungbinh[student]["math"])
                + float(self.diemtrungbinh[student]["literature"])
                + float(self.diemtrungbinh[student]["english"]) * 2
            )
            khoi_tunhien = [A, A1, B]
            for x in khoi_tunhien:
                if x >= 24:
                    result[student].append(1)
                elif x >= 18 and x < 24:
                    result[student].append(2)
                elif x >= 12 and x < 18:
                    result[student].append(3)
                elif x < 12:
                    result[student].append(4)
            if C >= 21:
                result[student].append(1)
            elif C >= 15 and C < 21:
                result[student].append(2)
            elif C >= 12 and C < 15:
                result[student].append(3)
            elif C < 12:
                result[student].append(4)
            if D >= 32:
                result[student].append(1)
            elif D >= 24 and D < 32:
                result[student].append(2)
            elif D >= 20 and D < 24:
                result[student].append(3)
            elif D < 20:
                result[student].append(4)
        print(result)
        return result


# Input:
# - Đường dẫn bảng điểm chi tiết cho từng môn của tất cả học sinh lưu
# trong file “diem_chitiet.txt”.
# - Đường dẫn để lưu output.
# Yêu cầu: Kết quả được lưu ra file “diem_trungbinh.txt” và “danhgia_hocsinh.txt”
# theo đường dẫn cho trước.


def main():
    # bangdiem = BANGDIEM(input_file = "./transcript.txt")
    # bangdiem_dict = bangdiem.tinhdiem_trungbinh()
    # bangdiem.luudiem_trungbinh(outputfile = "./diem_trungbinh_OOP.txt")

    DANHGIA(
        input_file="./transcript.txt",
        outputfile="./diem_trungbinh_OOP.txt",
        outputA="./danhgia_hocsinh_OOP.txt",
    )
    # danhgia_obj.xeploai_hocsinh()
    # danhgia_obj.xeploai_thidaihoc_hocsinh()
    # bangdiemA = BANGDIEM(intput_file="./tran scripy2.xt")
    # bangdictionary = bangdiemA.tinhdiem_trungbinh()
    # BANGDIEM.luudiem_trungbinh(dict_input = result, outputfile = "./diem_trungbinh_OOP.txt")
    # DANHGIA.xeploai_hocsinh(outputfile = "./“danhgia_hocsinh_OOP.txt")


# BANGDIEM.load_dulieu("./transcript.txt")

main()
